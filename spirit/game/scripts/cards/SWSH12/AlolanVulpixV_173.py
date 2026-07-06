from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ac16aea-9296-5604-b682-7e30d81feab6",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpixV.Name",
    display_name="Alolan Vulpix V",
    searchable_by=["Alolan Vulpix V", "Basic", "V", "AlolanVulpixV"],
    subtypes=["Basic", "V"],
    collector_number=173,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=37,
    abilities=[
        Attack(
            title="White Drop",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 50 more damage.",
            cost={},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)