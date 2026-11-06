from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive


async def stored_power(ctx):
    """30 damage. Move all Energy attached to this Pokémon to 1 Benched."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = list(ctx.attached_energies(ctx.attacker))
    if not bench or not energies:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to")
    if target is None:
        return
    for energy in energies:
        await ctx.move_energy(energy, target)


class VictoryStarPassive(Passive):
    """Once during your turn, after you flip coins for an attack, you may
    ignore those results and flip again (engine gates once/turn via
    turn_state.attack_coin_reroll_used)."""

    def offers_attack_coin_reroll(self, player_id, carrier, attacker=None):
        return player_id == carrier.owning_player_id


card = PokemonCardDef(
    guid="fc8ed3c7-8d44-56c7-9313-020bbda2fc34",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Ability(
            title="Victory Star",
            game_text="Once during your turn, after you flip any coins for an attack, you may ignore all effects of those coin flips and begin flipping those coins again. You can't use more than 1 Victory Star Ability each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=VictoryStarPassive(),
        ),
        Attack(
            title="Stored Power",
            game_text="Move all Energy attached to this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=stored_power,
        ),
    ],
)