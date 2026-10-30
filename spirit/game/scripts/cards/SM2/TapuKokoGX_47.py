from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.attacks_common import damage_per, count_energy

from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Triggers


async def aero_trail(ctx):
    """On play to Bench: move any Lightning Energy here; if you do, switch."""
    if not await ctx.ask_yes_no(
        "Move any number of Lightning Energy to this Pokémon and switch it into the Active Spot?"
    ):
        return
    moved = await ctx.move_energy_freely(
        [p for p in ctx.my_pokemon_in_play() if p is not ctx.source],
        [ctx.source],
        predicate=lambda e: energy_provides_type(e, PokemonTypes.LIGHTNING.value),
        prompt="Choose Lightning Energy to move to this Pokémon",
    )
    if not moved:
        return
    if ctx.source is ctx.my_active():
        return
    await ctx.switch_active(ctx.player_id, ctx.source)


card = PokemonCardDef(
    guid="e0c45b58-9cbd-5949-a2f7-b7165d785e39",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoGX.Name",
    display_name="Tapu Koko-GX",
    searchable_by=["Tapu Koko-GX", "Basic", "GX", "TapuKokoGX"],
    subtypes=["Basic", "GX"],
    collector_number=47,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=785,
    abilities=[
        Ability(
            title="Aero Trail",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may move any number of Lightning Energy from your other Pok\u00e9mon to this Pok\u00e9mon. If you do, switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=aero_trail,
        ),
        Attack(
            title="Sky-High Claws",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Tapu Thunder-GX",
            game_text="This attack does 50 damage times the amount of Energy attached to all of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy('opponent'), 50),
        ),
    ],
)