from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack


async def _electromagnetic_wall(ctx):
    """While this Pokemon is Active: whenever the opponent attaches an Energy
    from hand to one of their Pokemon, put 3 damage counters on it."""
    receiver = ctx.energy_receiver
    if ctx.attaching_player_id == ctx.player_id or receiver is None:
        return
    if ctx.source is not ctx.my_active() or receiver.owning_player_id == ctx.player_id:
        return
    await ctx.deal_damage(30, target=receiver, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="1f7087d1-64cc-55fc-93d9-6f523d6f215c",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=40,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Electromagnetic Wall",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever your opponent attaches an Energy from his or her hand to 1 of his or her Pok\u00e9mon, put 3 damage counters on that Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_electromagnetic_wall,
        ),
        Attack(
            title="Electrobullet",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=snipe_attack(20, also_base=True),
        ),
    ],
)