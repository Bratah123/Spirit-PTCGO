from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="05d1b2bb-e953-52bb-bc6e-70a7438cd858",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="TK1B",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 20 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=20, base=20),
        ),
    ],
)