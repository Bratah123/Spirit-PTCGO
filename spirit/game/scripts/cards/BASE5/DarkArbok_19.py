from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, spread_damage
from spirit.game.card_effects.ecard import stare


card = PokemonCardDef(
    guid="f0e38b6d-eb95-5bf1-ab37-796e4396fdcb",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkArbok.Name",
    display_name="Dark Arbok",
    searchable_by=["Dark Arbok", "Stage 1", "DarkArbok"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Stare",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.) If that Pok\u00e9mon has a Pok\u00e9mon Power, that power stops working until the end of your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2},
            effect=stare,
        ),
        Attack(
            title="Poison Vapor",
            game_text="The Defending Pok\u00e9mon is now Poisoned. This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 3},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, also=spread_damage(10)),
        ),
    ],
)
