from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.sm7 import (
    sandy_fear_gx,
)


card = PokemonCardDef(
    guid="bfdee004-8db0-539a-9c49-564b2b0429f1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalossandGX.Name",
    display_name="Palossand-GX",
    searchable_by=["Palossand-GX", "Stage 1", "GX", "PalossandGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=82,
    set_code="SM7",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=770,
    abilities=[
        Attack(
            title="Eerie Light",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Absorb Life",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=heal_attack(20),
        ),
        Attack(
            title="Sandy Fear-GX",
            game_text="Look at the top 13 cards of your opponent's deck and discard any number of Pok\u00e9mon you find there. This attack does 60 damage for each card you discarded in this way. Your opponent shuffles the other cards back into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=sandy_fear_gx,
        ),
    ],
)