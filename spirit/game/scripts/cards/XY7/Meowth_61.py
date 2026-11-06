from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_dark_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.DARKNESS.value)


def _has_dark(ctx):
    return any(_is_dark_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="79383333-6460-5cbe-8216-690624b6abfe",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Act Tough",
            game_text="If this Pok\u00e9mon has any Darkness Energy attached to it, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_has_dark, 20),
        ),
    ],
)