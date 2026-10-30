from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import extra_liquid_ex_passive, power_revenge_prizes_taken

card = PokemonCardDef(
    guid="9059ec8b-4b07-5d0e-918b-63c10291efa9",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptileex.Name",
    display_name="Sceptile ex δ",
    searchable_by=["Sceptile ex \u03b4", "Stage 2", "ex", "Sceptileex"],
    subtypes=["Stage 2", "ex"],
    collector_number=96,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Extra Liquid",
            game_text="Each player's Pok\u00e9mon-ex can't use any Pok\u00e9-Powers and pays Colorless more Energy to use its attacks. Each Pok\u00e9mon can't be affected by more than 1 Extra Liquid Pok\u00e9-Body.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=extra_liquid_ex_passive(),
            effect=None,
        ),
        Attack(
            title="Power Revenge",
            game_text="Does 60 damage plus 10 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
                        effect=power_revenge_prizes_taken(60, 10),
        ),
    ],
)