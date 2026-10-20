from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _stoke(ctx):
    """Flip a coin. If heads, search your deck for up to 3 basic Energy cards
    and attach them to this Pokemon. Shuffle."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not results or not results[0]:
        return
    picks = await ctx.search_deck(is_basic_energy_card, count=3, minimum=0,
                                  prompt="Choose up to 3 basic Energy cards")
    for card in picks or []:
        await ctx.attach_energy(card, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="3aa98978-4152-56d8-b85d-367fadb47e08",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    display_name="Charizard-EX",
    searchable_by=["Charizard-EX", "Basic", "EX", "CharizardEX"],
    subtypes=["Basic", "EX"],
    collector_number=11,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Stoke",
            game_text="Flip a coin. If heads, search your deck for up to 3 basic Energy cards and attach them to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_stoke,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)