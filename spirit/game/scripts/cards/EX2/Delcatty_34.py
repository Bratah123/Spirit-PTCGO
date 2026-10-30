from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.trainers import is_basic_energy_card


def _basic_energy_on_actives(ctx):
    total = 0
    for pokemon in (ctx.my_active(), ctx.opponent_active()):
        if pokemon is None:
            continue
        total += sum(
            1 for energy in ctx.attached_energies(pokemon)
            if is_basic_energy_card(energy)
        )
    return total


card = PokemonCardDef(
    guid="116cb9af-b443-5d08-ab98-ebb53648a36a",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Ultra Energy Source",
            game_text="Does 10 damage times the number of basic Energy cards attached to all of the Active Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="x",
            effect=damage_per(_basic_energy_on_actives, 10),
        ),
    ],
)
