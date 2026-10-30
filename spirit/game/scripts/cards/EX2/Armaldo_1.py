from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import both_players_cant_play_supporters


card = PokemonCardDef(
    guid="72f132b5-3ac7-5724-909c-7875ffffe35c",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name",
    display_name="Armaldo",
    searchable_by=["Armaldo", "Stage 2", "Armaldo"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    family_id=347,
    abilities=[
        Ability(
            title="Primal Veil",
            game_text="As long as Armaldo is your Active Pok\u00e9mon, each player can't play any Supporter Cards.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=both_players_cant_play_supporters(),
        ),
        Attack(
            title="Blade Arms",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
