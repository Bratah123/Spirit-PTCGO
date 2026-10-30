from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import has_energy_cards_attached, kindle


card = PokemonCardDef(
    guid="1c9feabb-2e52-5c00-9fc6-740e400c9601",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesCharmander.Name",
    display_name="Blaine's Charmander",
    searchable_by=["Blaine's Charmander", "Basic", "BlainesCharmander"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Kindle",
            game_text="Discard 1 Energy card attached to Blaine's Charmander in order to use this attack. If the Defending Pok\u00e9mon has any Energy cards attached to it, choose 1 of them and discard it.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            condition=has_energy_cards_attached(),
            effect=kindle,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
