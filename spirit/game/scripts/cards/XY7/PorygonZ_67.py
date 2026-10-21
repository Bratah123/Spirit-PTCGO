from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import devolve_depth


async def _digital_reboot(ctx):
    """Devolve as many of your Benched Pokemon as many times as you like; the
    removed Evolution cards go to your hand."""
    for _ in range(12):
        evolved = [p for p in ctx.my_bench() if devolve_depth(p) > 0]
        if not evolved:
            return
        target = await ctx.choose_pokemon(evolved, "Devolve which Benched Pokémon? (decline to stop)", optional=True)
        if target is None:
            return
        await ctx.devolve_pokemon(target, 1, destination="hand")


card = PokemonCardDef(
    guid="24dc9a73-f476-53e1-9544-cd2970ab7432",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        ancient_trait('θ Stop'),
        Attack(
            title="Digital Reboot",
            game_text="Devolve as many of your Benched Pok\u00e9mon as many times as you like. Put each Evolution card removed this way into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_digital_reboot,
        ),
        Attack(
            title="Dazzle Blast",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)