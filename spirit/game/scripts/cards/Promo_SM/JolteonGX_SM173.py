from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm8 import lava_burn
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="a58f79c2-8821-5282-aba7-9ccbec570120",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonGX.Name",
    display_name="Jolteon-GX",
    searchable_by=["Jolteon-GX", "Stage 1", "GX", "JolteonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=173,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Electrobullet",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=lava_burn,
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
        Attack(
            title="Swift Run-GX",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=protect_next_turn(prevent=True, effects_too=True),
        ),
    ],
)