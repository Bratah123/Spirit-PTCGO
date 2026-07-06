from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70959369-220f-5338-bdef-cfebe8044717",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic", "Palkia"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Ability(
            title="Absolute Space",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Stadium cards from their hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Overdrive Smash",
            game_text="During your next turn, this Pok\u00e9mon's Overdrive Smash attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)