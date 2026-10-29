from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import blow_away_bomb, balloon_burst

card = PokemonCardDef(
    guid="ea52abf8-6c07-5462-9601-591c19c3f0b3",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Blow-Away Bomb",
            game_text="Once during your turn, when you discard this Pok\u00e9mon with the effect of Roxie, you may put 1 damage counter on each of your opponent's Pok\u00e9mon. (Place damage counters after the effect of Roxie.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=blow_away_bomb,
        ),
        Attack(
            title="Balloon Burst",
            game_text="Discard this Pok\u00e9mon and all cards attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=balloon_burst,
        ),
    ],
)