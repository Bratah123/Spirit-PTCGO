from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


async def spiral_burst(ctx):
    """20, +80 for each basic Fire or basic Lightning Energy discarded from
    this Pokémon (up to 2 of one type)."""
    attacker = ctx.attacker
    attached = ctx.attached_energies(attacker)
    fire = [c for c in attached if is_basic_energy_card(c)
            and energy_provides_type(c, PokemonTypes.FIRE.value)]
    lightning = [c for c in attached if is_basic_energy_card(c)
                 and energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
    discarded = []
    if fire and lightning:
        choice = await ctx.choose(
            "Choose up to 2 Energy to discard from this Pokémon:",
            ["Basic Fire Energy", "Basic Lightning Energy"],
        )
        pool = fire if choice == 0 else lightning
        discarded = await ctx.choose_cards(
            pool, min(2, len(pool)), minimum=0,
            prompt="Choose up to 2 Energy to discard",
        )
    elif fire or lightning:
        pool = fire or lightning
        discarded = await ctx.choose_cards(
            pool, min(2, len(pool)), minimum=0,
            prompt="Choose up to 2 Energy to discard",
        )
    if discarded:
        await ctx.discard_cards(discarded)
    await ctx.deal_damage(20 + 80 * len(discarded))


card = PokemonCardDef(
    guid="d16443f5-fbbd-5dc0-9558-c703387cc38a",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaV.Name",
    display_name="Rayquaza V",
    searchable_by=["Rayquaza V", "Basic", "V", "Rapid Strike", "RayquazaV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=194,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=mill_attack(2, opponent=False),
        ),
        Attack(
            title="Spiral Burst",
            game_text="You may discard up to 2 basic Fire Energy or up to 2 basic Lightning Energy from this Pokémon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=spiral_burst,
        ),
    ],
)
