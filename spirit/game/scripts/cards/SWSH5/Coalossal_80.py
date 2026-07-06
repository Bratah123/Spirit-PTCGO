from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb5c9e14-9d56-5c4f-8285-51f84de6ca01",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Coalossal.Name",
    display_name="Coalossal",
    searchable_by=["Coalossal", "Stage 2", "Coalossal"],
    subtypes=["Stage 2"],
    collector_number=80,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Coal Cannon",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 90 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)