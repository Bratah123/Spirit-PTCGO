from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="3ef45852-2727-57a8-8699-42f703890ced",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    display_name="Trumbeak",
    searchable_by=["Trumbeak", "Stage 1", "Trumbeak"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    family_id=731,
    abilities=[
        Attack(
            title="Bullet Seed",
            game_text="Flip 4 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)