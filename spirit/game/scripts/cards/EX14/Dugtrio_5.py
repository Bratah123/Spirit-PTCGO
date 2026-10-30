from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import double_edge_recoil, sand_veil_bench_protect, telekinesis_snipe


card = PokemonCardDef(
    guid="0b324c26-e4e7-59a9-bbbc-f6ebaf3613e4",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Dugtrio"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Sand Veil",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=sand_veil_bench_protect(),
            effect=None,
        ),
        Attack(
            title="Dig Under",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=telekinesis_snipe(30),
        ),
        Attack(
            title="Double-edge",
            game_text="Dugtrio does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
                        effect=double_edge_recoil(10),
        ),
    ],
)