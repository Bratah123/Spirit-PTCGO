from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.session.legal_actions import energy_provided_count


def _both_actives_energy(ctx):
    total = 0
    for pokemon in (ctx.my_active(), ctx.opponent_active()):
        if pokemon is None:
            continue
        for energy in ctx.attached_energies(pokemon):
            total += energy_provided_count(energy)
    return total


card = PokemonCardDef(
    guid="a45d39b9-d278-5dd8-83f1-0ba97c38f8a0",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewV.Name",
    display_name="Mew V",
    searchable_by=["Mew V", "Basic", "V", "MewV"],
    subtypes=["Basic", "V"],
    collector_number=69,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    abilities=[
        Attack(
            title="X Ball",
            game_text="This attack does 30 damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(_both_actives_energy, 30),
        ),
    ],
)