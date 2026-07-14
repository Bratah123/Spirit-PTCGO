from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents

card = PokemonCardDef(
    guid="c468307d-1d94-50b5-8009-902658cf8cc7",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name="Yanma",
    searchable_by=["Yanma", "Basic", "Yanma"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="CZ",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=193,
    abilities=[
        Attack(
            title="Swoop Across",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(10),
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)