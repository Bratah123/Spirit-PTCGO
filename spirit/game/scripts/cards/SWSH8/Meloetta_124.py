from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per


def _fusion_strike_energy_count(ctx):
    total = 0
    for pokemon in ctx.my_pokemon_in_play():
        for energy in ctx.attached_energies(pokemon):
            if "Fusion Strike" in subtypes_for(energy.archetype_id):
                total += 1
    return total


card = PokemonCardDef(
    guid="416d73c5-8c62-5d88-a94f-564673022e2e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic", "Fusion Strike", "Meloetta"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=124,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=648,
    abilities=[
        Attack(
            title="Melodious Echo",
            game_text="This attack does 70 damage for each Fusion Strike Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=damage_per(_fusion_strike_energy_count, 70),
        ),
    ],
)