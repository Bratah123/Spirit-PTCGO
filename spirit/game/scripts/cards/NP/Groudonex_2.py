from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    self_energy_discard_attack, spread_damage,
)


card = PokemonCardDef(
    guid="593a0993-c363-5349-a1eb-42f314a8c31a",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "ex", "Groudonex"],
    subtypes=["Basic", "ex"],
    collector_number=2,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Major Earthquake",
            game_text="Discard a Fighting Energy card attached to Groudon ex. Does 10 damage to your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 4},
            damage=80,
            effect=self_energy_discard_attack(
                count=1, energy_type=PokemonTypes.FIGHTING,
                also=spread_damage(10, side="mine", also_base=False),
            ),
        ),
    ],
)
