export const fetchData = async (countryCode) => {
    try {
        const response = await fetch(`/countrypopup/${countryCode}`)
        const jsonData = await response.json()
        return jsonData
    } catch (error) {
        console.error('Error fetching data:', error)
        return null
    }
}
