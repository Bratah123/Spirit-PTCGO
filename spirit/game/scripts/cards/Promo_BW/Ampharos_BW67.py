from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import energy_provides_type


async def _electricannon(ctx):
    """You may discard all Lightning Energy attached to this Pokemon. If you
    do, this attack does 60 more damage."""
    me = ctx.attacker
    lightning = [e for e in ctx.attached_energies(me) if energy_provides_type(e, PokemonTypes.LIGHTNING.value)]
    bonus = 0
    if lightning and await ctx.ask_yes_no("Discard all Lightning Energy for 60 more damage?"):
        await ctx.discard_cards(lightning)
        bonus = 60
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="d3bb2e2d-c83b-54ed-8e83-c25ac74578de",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=181,
    abilities=[
        Attack(
            title="Random Spark",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=snipe_attack(30, pool='any', count=1),
        ),
        Attack(
            title="Electricannon",
            game_text="You may discard all Lightning Energy attached to this Pok\u00e9mon. If you do, this attack does 60 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=_electricannon,
        ),
    ],
)