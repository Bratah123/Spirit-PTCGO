from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    major_tsunami, major_tsunami_condition, rending_jaws,
)


card = PokemonCardDef(
    guid="eafd87f7-bbb1-55bb-9145-b973c7ba1a4f",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Major Tsunami",
            game_text="Once during your turn (before your attack), if Feraligatr is your Active Pok\u00e9mon and if your opponent has any Benched Pok\u00e9mon, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon. Either way, if you have any Benched Pok\u00e9mon, switch Feraligatr with 1 of them. This power can't be used if Feraligatr is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=major_tsunami_condition,
            effect=major_tsunami,
        ),
        Attack(
            title="Rending Jaws",
            game_text="If here are no damage counters on the Defending Pok\u00e9mon, this attack's base damage is 40 instead of 70.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=rending_jaws,
        ),
    ],
)
