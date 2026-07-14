from spirit.game.card_effects.pokemon import double_dip_fangs, wild_tackle
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e20fb239-5125-50b6-bfe0-f9a8d899edfd",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StoutlandV.Name",
    display_name="Stoutland V",
    searchable_by=["Stoutland V", "Basic", "V", "StoutlandV"],
    subtypes=["Basic", "V"],
    collector_number=116,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=508,
    abilities=[
        Attack(
            title="Double Dip Fangs",
            game_text="If your opponent's Basic Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=double_dip_fangs,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=wild_tackle,
        ),
    ],
)
