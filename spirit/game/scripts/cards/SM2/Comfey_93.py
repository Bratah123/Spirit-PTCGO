from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import Triggers

from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.models.board import BoardState


def _fairy_energy_immune(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.FAIRY.value)
               for e in BoardState.attached_energies(target))


async def flower_shield(ctx):
    """Cure Special Conditions on your Pokémon that have Fairy Energy."""
    if ctx.energy_receiver is not None:
        targets = [ctx.energy_receiver]
    else:
        targets = ctx.my_pokemon_in_play()
    for pokemon in targets:
        if pokemon is None or pokemon.owning_player_id != ctx.player_id:
            continue
        if any(energy_provides_type(e, PokemonTypes.FAIRY.value)
               for e in ctx.attached_energies(pokemon)):
            await ctx.cure_all_conditions(pokemon)


async def sweet_kiss(ctx):
    """30 damage; the opponent draws a card."""
    await ctx.deal_damage()
    await ctx.draw_cards(1, ctx.opponent_id)


card = PokemonCardDef(
    guid="21fcddc6-697c-5923-b9b1-3d7e21e78f49",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic", "Comfey"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=764,
    abilities=[
        Ability(
            title="Flower Shield",
            game_text="Each of your Pok\u00e9mon that has any Fairy Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=(Triggers.ON_PLAY, Triggers.ON_ENERGY_ATTACHED), passive=condition_immunity_passive(protects=_fairy_energy_immune),
            effect=flower_shield,
        ),
        Attack(
            title="Sweet Kiss",
            game_text="Your opponent draws a card.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=sweet_kiss,
        ),
    ],
)