from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.card_effects.ecard import snatch


card = PokemonCardDef(
    guid="608c4aa7-d8bb-50ef-87dc-54f774dada8f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=171,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Ability(
            title="Poison Resistance",
            game_text="Scizor can't be Poisoned.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=condition_immunity_passive(SpecialConditions.POISONED),
        ),
        Attack(
            title="Snatch",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon with no damage counters on it and switch the Defending Pok\u00e9mon with it.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=snatch,
        ),
        Attack(
            title="Heavy Metal",
            game_text="Flip a number of coins equal to the amount of Metal Energy attached to Scizor. This attack does 30 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=flip_damage(
                coins_from=count_energy("self", PokemonTypes.METAL),
                bonus_per_heads=20,
            ),
        ),
    ],
)
