from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, bonus_if, has_tool


card = PokemonCardDef(
    guid="a5ce82e0-5b7f-5ca5-a5fd-0c402234bc90",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
        Attack(
            title="Reinforced Nose",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 50 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bonus_if(lambda ctx: has_tool(ctx.attacker), 50),
        ),
    ],
)