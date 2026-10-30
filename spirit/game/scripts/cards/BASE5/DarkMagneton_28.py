from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import dark_magnetic_lines, no_weakness_or_resistance


card = PokemonCardDef(
    guid="07dff565-eaab-590c-94d1-8fa32f6ed077",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMagneton.Name",
    display_name="Dark Magneton",
    searchable_by=["Dark Magneton", "Stage 1", "DarkMagneton"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Sonicboom",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=no_weakness_or_resistance,
        ),
        Attack(
            title="Magnetic Lines",
            game_text="If the Defending Pok\u00e9mon has any basic Energy cards attached to it, choose 1 of them. If your opponent has any Benched Pok\u00e9mon, choose 1 of them and attach that Energy card to it.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            effect=dark_magnetic_lines,
        ),
    ],
)
