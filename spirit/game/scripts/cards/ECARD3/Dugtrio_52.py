from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="b0aaae04-4482-5e62-9ff0-a9478a2593fa",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Dugtrio"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Burrow",
            game_text="Flip a coin. If heads, prevent all damage done by attacks to Dugtrio during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Dig Under",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. Don't apply Weakness or Resistance. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(30, pool="any", apply_modifiers=False),
        ),
    ],
)
