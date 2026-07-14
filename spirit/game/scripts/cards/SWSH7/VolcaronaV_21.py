from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


async def surging_flames(ctx):
    """20 more damage per basic Energy in your discard; then shuffle those Energy into your deck."""
    energy_cards = [c for c in ctx.discard_pile(ctx.player_id) if is_basic_energy_card(c)]
    await ctx.deal_damage(20 + 20 * len(energy_cards))
    if energy_cards:
        await ctx.shuffle_into_deck(energy_cards, player_id=ctx.player_id)


fire_blast = self_energy_discard_attack(count=1)

card = PokemonCardDef(
    guid="af98160a-b9bc-53aa-92ca-5ede1e0ad8e9",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcaronaV.Name",
    display_name="Volcarona V",
    searchable_by=["Volcarona V", "Basic", "V", "VolcaronaV"],
    subtypes=["Basic", "V"],
    collector_number=21,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=637,
    abilities=[
        Attack(
            title="Surging Flames",
            game_text="This attack does 20 more damage for each basic Energy card in your discard pile. Then, shuffle those Energy cards into your deck.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=surging_flames,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=fire_blast,
        ),
    ],
)