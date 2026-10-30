from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import flotation_low_energy_retreat, hydro_shot_discard_snipe

card = PokemonCardDef(
    guid="13be8569-a8d7-5ed7-825a-273e4222b02c",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "ex", "Kyogreex"],
    subtypes=["Basic", "ex"],
    collector_number=95,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Ability(
            title="Flotation",
            game_text="As long as Kyogre ex has 1 Energy or less attached to it, the Retreat Cost for each of your Kyogre ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=flotation_low_energy_retreat(),
            effect=None,
        ),
        Attack(
            title="Hydro Shot",
            game_text="Discard 2 Energy attached to Kyogre ex. Choose 1 of your opponent's Pok\u00e9mon. This attack does 70 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
                        effect=hydro_shot_discard_snipe(70, 2),
        ),
    ],
)