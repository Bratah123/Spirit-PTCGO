from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35f15b60-54b5-59f0-941c-64a13c2093c2",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantJirachi.Name",
    display_name="Radiant Jirachi",
    searchable_by=["Radiant Jirachi", "Basic", "Radiant", "RadiantJirachi"],
    subtypes=["Basic", "Radiant"],
    collector_number=120,
    set_code="SWSH12",
    rarity=Rarities.RareRadiant,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=385,
    abilities=[
        Ability(
            title="Entrusted Wishes",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Astral Misfortune",
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)