from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import (
    ancient_wisdom, ancient_wisdom_condition, gigaton_break,
)

card = PokemonCardDef(
    guid="3d7ec5c6-6fe1-56e3-b408-0565d1a271c0",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Ability(
            title="Ancient Wisdom",
            game_text="Once during your turn, if you have Regirock, Regice, Registeel, Regieleki, and Regidrago in play, you may attach up to 3 Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=ancient_wisdom_condition,
            effect=ancient_wisdom,
        ),
        Attack(
            title="Gigaton Break",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon VMAX, this attack does 150 more damage.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=150,
            damage_operator="+",
            effect=gigaton_break,
        ),
    ],
)
