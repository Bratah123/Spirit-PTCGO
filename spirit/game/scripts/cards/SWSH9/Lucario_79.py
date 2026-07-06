from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2bd1d15a-29ba-5870-9b34-3ed6be0f3294",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Roaring Resolve",
            game_text="Once during your turn, you may put 2 damage counters on this Pok\u00e9mon. If you do, search your deck for a Fighting Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Aura Sphere Volley",
            game_text="Discard all Fighting Energy from this Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)