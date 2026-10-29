from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    zappy_pom_poms,
)

card = PokemonCardDef(
    guid="cffe5289-e80d-56dc-9819-2ca577224e0e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Attack(
            title="Zappy Pom-Poms",
            game_text="This attack does 30 damage to each Pok\u00e9mon-GX and Pok\u00e9mon-EX (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=zappy_pom_poms,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)