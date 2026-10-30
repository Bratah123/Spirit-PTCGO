from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import cross_cut, hoard_tools

card = PokemonCardDef(
    guid="651ce842-ab0d-5157-966e-4b5e3b94a771",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic", "Farfetchd"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=83,
    abilities=[
        Attack(
            title="Hoard",
            game_text="Search your deck for up to 2 Pok\u00e9mon Tool cards and attach them to any of your Pok\u00e9mon (excluding Pok\u00e9mon that already have a Pok\u00e9mon Tool attached to them). Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=hoard_tools(),
        ),
        Attack(
            title="Cross-Cut",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=cross_cut(10, 10),
        ),
    ],
)