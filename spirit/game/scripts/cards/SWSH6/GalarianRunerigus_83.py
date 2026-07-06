from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e34bc62-a849-5422-8c34-435bde640931",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRunerigus.Name",
    display_name="Galarian Runerigus",
    searchable_by=["Galarian Runerigus", "Stage 1", "GalarianRunerigus"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianYamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Spiteful Slate",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon VMAX (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)