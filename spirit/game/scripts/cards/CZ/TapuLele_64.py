from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.session.legal_actions import energy_provided_count


def _both_actives_energy(ctx) -> int:
    total = 0
    for pokemon in (ctx.my_active(), ctx.opponent_active()):
        if pokemon is None:
            continue
        for energy in ctx.attached_energies(pokemon):
            total += energy_provided_count(energy)
    return total


card = PokemonCardDef(
    guid="74defd7b-ac79-59df-a51d-9f8e3803f68a",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLele.Name",
    display_name="Tapu Lele",
    searchable_by=["Tapu Lele", "Basic", "TapuLele"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=786,
    abilities=[
        Attack(
            title="Energy Burst",
            game_text="This attack does 20 damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(_both_actives_energy, 20),
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=heal_attack(amount=30, target="self"),
        ),
    ],
)