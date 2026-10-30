from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    self_energy_discard_attack, spread_damage,
)


card = PokemonCardDef(
    guid="b8f84ba8-14ae-5294-bf44-23cd8d55539c",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "ex", "Kyogreex"],
    subtypes=["Basic", "ex"],
    collector_number=1,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Major Flood",
            game_text="Discard a Water Energy card attached to Kyogre ex. Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=60,
            effect=self_energy_discard_attack(
                count=1, energy_type=PokemonTypes.WATER,
                also=spread_damage(10, side="both", also_base=False),
            ),
        ),
    ],
)
