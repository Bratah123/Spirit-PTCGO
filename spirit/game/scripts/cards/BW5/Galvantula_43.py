from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16f492ca-589f-5744-a665-3c725958974d",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Quick Turn",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Electrisilk",
            game_text="If the Defending Pok\u00e9mon has no Retreat Cost, this attack does 40 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)