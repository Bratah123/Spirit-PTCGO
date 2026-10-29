from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _dragon_wave(ctx):
    """130; discard a Grass Energy and a Lightning Energy from this Pokemon."""
    await ctx.deal_damage()
    for pred, label in ((_is_grass_energy, "Grass"), (_is_lightning_energy, "Lightning")):
        if any(pred(e) for e in ctx.attached_energies(ctx.attacker)):
            await ctx.discard_energy_from(ctx.attacker, 1, predicate=pred, minimum=1,
                                          prompt=f"Discard a {label} Energy")


card = PokemonCardDef(
    guid="b33a1582-e923-532f-bb0a-37d4e3150744",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Dragon Wave",
            game_text="Discard a Grass Energy and a Lightning Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1},
            damage=130,
            effect=_dragon_wave,
        ),
        Attack(
            title="Giant Tail",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=200,
            effect=flip_or_nothing(),
        ),
    ],
)