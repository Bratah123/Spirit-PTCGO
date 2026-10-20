from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="717fd228-2b05-5c0c-a1b3-31513b4746ba",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1", "Jolteon"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Electrigun",
            game_text="You may discard a Lightning Energy attached to this Pok\u00e9mon. If you do, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)