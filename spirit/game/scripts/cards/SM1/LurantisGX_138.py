from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _flower_supply(ctx):
    """40; attach 2 basic Energy cards from your discard pile to your Pokemon in any way you like."""
    await ctx.deal_damage()
    for _ in range(2):
        cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        mine = ctx.my_pokemon_in_play()
        if not cards or not mine:
            return
        picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a basic Energy card")
        if not picks:
            return
        target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach it to which Pokémon?")
        await ctx.attach_energy(picks[0], target or mine[0])


card = PokemonCardDef(
    guid="bfbae821-3b85-540e-85a2-e7a887fde0ad",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LurantisGX.Name",
    display_name="Lurantis-GX",
    searchable_by=["Lurantis-GX", "Stage 1", "GX", "LurantisGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=138,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=753,
    abilities=[
        Attack(
            title="Flower Supply",
            game_text="Attach 2 basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=_flower_supply,
        ),
        Attack(
            title="Solar Blade",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=heal_attack(30),
        ),
        Attack(
            title="Chloroscythe-GX",
            game_text="This attack does 50 damage times the amount of Grass Energy attached to this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.GRASS), 50),
        ),
    ],
)