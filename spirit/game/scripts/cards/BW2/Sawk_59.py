from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, lock_all_attacks


async def _lock_self(ctx):
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="9cd21e8b-72cc-5f28-9e9c-2f7550e99f11",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic", "Sawk"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Five Fierce Chops",
            game_text="Flip 5 coins. This attack does 20 damage times the number of heads. This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(5, per_heads=20, also=_lock_self),
        ),
    ],
)
