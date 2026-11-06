from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import energy_bomb


card = PokemonCardDef(
    guid="ac91ad10-7a1e-5e6c-b41a-df0691dd0421",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkElectrode.Name",
    display_name="Dark Electrode",
    searchable_by=["Dark Electrode", "Stage 1", "DarkElectrode"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Energy Bomb",
            game_text="Take all Energy cards attached to Dark Electrode and attach them to your Benched Pok\u00e9mon (in any way you choose). If you have no Benched Pok\u00e9mon, discard all Energy cards attached to Dark Electrode.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            effect=energy_bomb,
        ),
    ],
)
