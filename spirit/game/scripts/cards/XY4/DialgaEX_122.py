from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks, self_energy_discard_attack
from spirit.game.content.definitions import def_for


async def _chrono_wind(ctx):
    """60; if the Defending Pokemon is a Pokemon-EX, it can't attack during
    your opponent's next turn."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and "EX" in (getattr(def_for(d.archetype_id), "subtypes", None) or []):
        lock_defender_attacks(ctx, d)


card = PokemonCardDef(
    guid="176fe8f3-2ed6-5d64-81db-93c2001a4ba4",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaEX.Name",
    display_name="Dialga-EX",
    searchable_by=["Dialga-EX", "Basic", "EX", "DialgaEX"],
    subtypes=["Basic", "EX"],
    collector_number=122,
    set_code="XY4",
    rarity=Rarities.RareSecret,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title="Chrono Wind",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon-EX, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_chrono_wind,
        ),
        Attack(
            title="Full Metal Impact",
            game_text="Discard 2 Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.METAL),
        ),
    ],
)