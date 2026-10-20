from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import energy_provides_type, is_energy_card
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.models.board import BoardState


async def verdant_wind(ctx):
    """Cures Special Conditions the moment one of your Pokemon picks up
    Grass Energy; the passive keeps it immune from then on."""
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id != ctx.player_id:
        return
    if not energy_provides_type(ctx.attached_energy, PokemonTypes.GRASS.value):
        return
    await ctx.cure_all_conditions(receiver)


def _grass_energy_immune(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.GRASS.value)
               for e in BoardState.attached_energies(target))


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


async def _emerald_slash(ctx):
    """Printed damage; you may search your deck for 2 Grass Energy cards and
    attach them to 1 of your Benched Pokemon. Shuffle."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench or not await ctx.ask_yes_no("Search your deck for 2 Grass Energy cards?"):
        return
    picks = await ctx.search_deck(_is_grass_energy, count=2, minimum=0,
                                  prompt="Choose up to 2 Grass Energy cards")
    if picks:
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to attach them to")
        for card in picks:
            await ctx.attach_energy(card, target or bench[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="5f7afba7-3ac5-5651-babb-752919414391",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionEX.Name",
    display_name="Virizion-EX",
    searchable_by=["Virizion-EX", "Basic", "EX", "VirizionEX"],
    subtypes=["Basic", "EX"],
    collector_number=96,
    set_code="BW10",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=640,
    abilities=[
        Ability(
            title="Verdant Wind",
            game_text="Each of your Pok\u00e9mon that has any Grass Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pok\u00e9mon.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=verdant_wind,
            passive=condition_immunity_passive(protects=_grass_energy_immune),
        ),
        Attack(
            title="Emerald Slash",
            game_text="You may search your deck for 2 Grass Energy cards and attach them to 1 of your Benched Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_emerald_slash,
        ),
    ],
)