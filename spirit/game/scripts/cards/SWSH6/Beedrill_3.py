from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.effects import is_special_energy


async def persist_sting(ctx):
    """If the opponent's Active has any Special Energy attached, it is Knocked Out."""
    defender = ctx.defender
    if defender is not None and any(
        is_special_energy(e) for e in ctx.attached_energies(defender)
    ):
        await ctx.knock_out(defender)


card = PokemonCardDef(
    guid="3e741793-cbf8-50c9-9947-4d303a67c51d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Single Strike", "Beedrill"],
    subtypes=["Stage 2", "Single Strike"],
    collector_number=3,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Persist Sting",
            game_text="If your opponent's Active Pokémon has any Special Energy attached, it is Knocked Out.",
            cost={PokemonTypes.GRASS: 1},
            effect=persist_sting,
        ),
        Attack(
            title="Jet Spear",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=110,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
